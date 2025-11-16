#import "@preview/badgery:0.1.1": badge-gray, badge-green, badge-red, badge-yellow
#import "@preview/cades:0.3.1": qr-code
#import "@preview/polylux:0.4.0": *

#let exp(qty) = {
  h(1fr)
  badge-green("+" + str(qty) + "exp")
}

#let difficulty(lvl) = {
  h(1fr)

  if lvl == 1 {
    badge-green(sym.star)
  } else if lvl == 2 {
    badge-yellow(sym.star + sym.star)
  } else if lvl == 3 {
    badge-red(sym.star + sym.star + sym.star)
  } else if lvl == 4 {
    badge-red(sym.star + sym.star + sym.star + sym.star)
  } else {
    panic("Invalid difficulty level: " + str(lvl))
  }
}

#let slidew(
  slide_title: str,
  title: str,
  level: 0,
  course: str,
  author: str,

  body
) = {
  set page(
    margin: 2cm,
    footer: align(bottom,
      toolbox.full-width-block(fill: rgb("#035a75"), inset: 8pt)[
        #align(center)[
          #text(fill: white, 10pt, title + " - " + course + " - " + author)
        ]
      ]
    ),
  )

  if level == 0 {
    heading(slide_title)
  } else {
    heading(slide_title + difficulty(level))
  }

  v(1em)

  body
}

#let center_url(url) = {
  align(center)[ *#url* ]
}

#let url_with_qr(url, height: 65%) = {
  align(center)[
    #qr-code(url, height: height)
  ]
  center_url(url)
}
