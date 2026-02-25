#import "@preview/polylux:0.4.0": *

#let slide_cover(
  title: str,
  course: str,
  description: str,
  author: str,
  email: str,
) = {
  slide[
    #set text(fill: white)
    #set page(fill: rgb("#035a75"))

    #align(right, [
      #block([
        #align(right)[
          #image("../images/logo-volpato.png", width: 30%)
        ]
      ])
    ])

    #v(2.5em)

    #text(weight: 700, 20pt, course)
    #v(1pt)
    #text(weight: 700, top-edge: 0pt, 40pt, title)
    #v(0.3em)
    #text(18pt, description)

    #pad(
      x: 0.1em,
      grid(
        gutter: 0.8em,
        columns: 2,
        text(weight: "bold", 16pt, "Docente:"),
        text(16pt, author + " " + sym.angle.l + email + sym.angle.r),
      )
    )
  ]
}

#let handout_cover(
  title: str,
  course: str,
  description: str,
  author: str,
  email: str,
) = {
  set text(size: 10pt, fill: white)

  set par(leading: 0.65em, justify: true)
  set page(numbering: none, number-align: center, fill: rgb("#035a75"), margin: (top: 1.5in, rest: 2in))
  set page(margin: 0.5in)

  align(right, [
    #block([
      #align(right)[
        #image("../images/logo-volpato.png", width: 30%)
      ]
    ])
  ])

  v(2em)

  text(weight: 700, 18pt, course)
  linebreak()
  text(weight: 700, 26pt, title)

  v(2em)

  text(description)
  v(1em)
  pad(
    x: 0.1em,
    grid(
      gutter: 0.8em,
      columns: 2,
      text(weight: "bold", "Docente:"),
      text(author + " " + sym.chevron.l + email + sym.chevron.r),
    )
  )

  place(
    bottom,
    dx: -7%,
    dy: 5%,
    image(
      "../images/code_cover.jpg",
      width: 115%
    )
  )

  pagebreak()
}
