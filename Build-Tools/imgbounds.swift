// imgbounds <image>: the picture's content edges, ignoring transparent and near-white margins, printed as the
// srcRect crop PowerPoint uses (left top right bottom, in 1/1000 of a percent). deck_pair.py addpics uses it so a
// generated diagram with wide empty margins fills its space on the slide (2026-10-01).
import Foundation
import CoreGraphics
import ImageIO

let a = CommandLine.arguments
guard a.count > 1, let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: a[1]) as CFURL, nil),
      let img = CGImageSourceCreateImageAtIndex(src, 0, nil) else { print("0 0 0 0"); exit(0) }
let w = img.width, h = img.height
var px = [UInt8](repeating: 0, count: w * h * 4)
guard let ctx = CGContext(data: &px, width: w, height: h, bitsPerComponent: 8, bytesPerRow: w * 4, space: CGColorSpaceCreateDeviceRGB(),
                          bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { print("0 0 0 0"); exit(0) }
ctx.draw(img, in: CGRect(x: 0, y: 0, width: w, height: h))
func ink(_ x: Int, _ y: Int) -> Bool {
    let i = (y * w + x) * 4
    let r = Int(px[i]), g = Int(px[i + 1]), b = Int(px[i + 2]), al = Int(px[i + 3])
    if al < 24 { return false }                                    // transparent
    return !(r > 240 && g > 240 && b > 240)                        // near white
}
var minX = w, minY = h, maxX = -1, maxY = -1
for y in stride(from: 0, to: h, by: 2) { for x in stride(from: 0, to: w, by: 2) where ink(x, y) {
    minX = min(minX, x); maxX = max(maxX, x); minY = min(minY, y); maxY = max(maxY, y) } }
guard maxX > minX, maxY > minY else { print("0 0 0 0"); exit(0) }
// a little air around the content; rows count from the top in the bitmap
let padX = w / 60, padY = h / 60
let l = max(0, minX - padX), r = min(w, maxX + padX), t = max(0, minY - padY), b = min(h, maxY + padY)
func k(_ v: Int, _ of: Int) -> Int { Int((Double(v) / Double(of) * 100000).rounded()) }
print(k(l, w), k(t, h), k(w - r, w), k(h - b, h))
