import unittest
import tempfile
import shutil
from pathlib import Path
from smart_organizer import SmartOrganizer, FileClassifier, UnsupportedExtensionError

class TestSmartOrganizer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory structure for each test
        self.test_dir = tempfile.mkdtemp()
        self.root = Path(self.test_dir)
        self.organizer = SmartOrganizer()
    
    def tearDown(self):
        # Clean up
        shutil.rmtree(self.test_dir)

    def test_classifier_correct(self):
        """Level 3 check: Correct classification of file types."""
        classifier = FileClassifier()
        
        cases = {
            "photo.jpg": "Immagini",
            "document.pdf": "Documenti",
            "song.mp3": "Musica",
            "movie.mp4": "Video",
            "archive.zip": "Archivi"
        }
        
        for filename, expected_folder in cases.items():
            path = self.root / filename
            dest = classifier.classify(path)
            self.assertEqual(dest.name, expected_folder, f"Failed to classify {filename}")

    def test_classifier_unsupported(self):
        """Level 3 check: Handle unsupported extensions."""
        classifier = FileClassifier()
        path = self.root / "unknown.xyz"
        with self.assertRaises(UnsupportedExtensionError):
            classifier.classify(path)
            
    def test_classifier_no_extension(self):
        """Level 3 check: Handle files with no extension."""
        classifier = FileClassifier()
        path = self.root / "README"
        with self.assertRaises(UnsupportedExtensionError):
            classifier.classify(path)

    def test_organization_success(self):
        """Level 3 check: Sort files into appropriate folders."""
        # Create dummy files
        files_to_create = ["pic.png", "notes.txt", "video.avi"]
        for f in files_to_create:
            (self.root / f).touch()

        # Run organizer
        self.organizer.organize(self.root)

        # Verify moves
        self.assertTrue((self.root / "Immagini" / "pic.png").exists())
        self.assertTrue((self.root / "Documenti" / "notes.txt").exists())
        self.assertTrue((self.root / "Video" / "video.avi").exists())
        
        # Verify original files are gone from root
        for f in files_to_create:
            self.assertFalse((self.root / f).exists())

    def test_organization_mixed_content(self):
        """Level 3 check: Handle mixed content including unsupported files."""
        # Create supported and unsupported files
        (self.root / "supported.jpg").touch()
        (self.root / "unsupported.abc").touch()
        
        self.organizer.organize(self.root)
        
        # Check files
        self.assertTrue((self.root / "Immagini" / "supported.jpg").exists())
        self.assertTrue((self.root / "unsupported.abc").exists()) # Should remain

if __name__ == '__main__':
    unittest.main()
