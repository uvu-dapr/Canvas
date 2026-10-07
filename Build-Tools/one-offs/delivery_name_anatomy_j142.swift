import AppKit
// The parts of a delivery file name (Recording Academy P&E Wing naming), one colored block per part with its label under it
let W = 1600, H = 560
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: W, pixelsHigh: H, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState(); NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
NSColor.white.setFill(); NSRect(x: 0, y: 0, width: W, height: H).fill()
func text(_ s: String, _ f: NSFont, _ c: NSColor, center: CGFloat, y: CGFloat) {
    let a = NSAttributedString(string: s, attributes: [.font: f, .foregroundColor: c]); let w = a.size().width
    a.draw(at: NSPoint(x: center - w / 2, y: y))
}
let title = NSFont.boldSystemFont(ofSize: 40)
text("Anatomy of a delivery file name", title, NSColor(calibratedWhite: 0.13, alpha: 1), center: CGFloat(W) / 2, y: CGFloat(H) - 80)
let parts: [(String, String, String, NSColor)] = [
    ("JS", "Artist", "initials", NSColor(calibratedRed: 0.05, green: 0.28, blue: 0.63, alpha: 1)),
    ("_", "", "", .clear),
    ("HorseNotHome", "Song title", "no spaces, under 15", NSColor(calibratedRed: 0.11, green: 0.37, blue: 0.13, alpha: 1)),
    ("_", "", "", .clear),
    ("AW03", "Mixer + mix", "initials, revision 03", NSColor(calibratedRed: 0.75, green: 0.21, blue: 0.05, alpha: 1)),
    ("_", "", "", .clear),
    ("VocalUp", "Version", "or stem name", NSColor(calibratedRed: 0.42, green: 0.11, blue: 0.60, alpha: 1)),
    ("_", "", "", .clear),
    ("44k16", "Format", "sample rate, bits", NSColor(calibratedRed: 0.0, green: 0.38, blue: 0.40, alpha: 1)),
    (".wav", "Extension", "the only period", NSColor(calibratedWhite: 0.35, alpha: 1)),
]
let mono = NSFont(name: "Menlo-Bold", size: 46)!
let small = NSFont.boldSystemFont(ofSize: 26), tiny = NSFont.systemFont(ofSize: 22)
let widths = parts.map { NSAttributedString(string: $0.0, attributes: [.font: mono]).size().width + ($0.3 == .clear ? 8 : 40) }
var x = (CGFloat(W) - widths.reduce(0, +)) / 2
let by: CGFloat = 270, bh: CGFloat = 92
for (i, p) in parts.enumerated() {
    let w = widths[i]
    if p.3 != .clear {
        let r = NSRect(x: x, y: by, width: w - 8, height: bh)
        p.3.setFill(); NSBezierPath(roundedRect: r, xRadius: 12, yRadius: 12).fill()
        text(p.0, mono, .white, center: r.midX, y: by + 20)
        text(p.1, small, p.3, center: r.midX, y: by - 52)
        text(p.2, tiny, NSColor(calibratedWhite: 0.3, alpha: 1), center: r.midX, y: by - 86)
    } else {
        text(p.0, mono, NSColor(calibratedWhite: 0.2, alpha: 1), center: x + w / 2 - 4, y: by + 20)
    }
    x += w
}
text("Underscores separate the parts. Capitalize each word. Dates, when used, are ISO: 20261007.", tiny, NSColor(calibratedWhite: 0.25, alpha: 1), center: CGFloat(W) / 2, y: 60)
NSGraphicsContext.restoreGraphicsState()
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
