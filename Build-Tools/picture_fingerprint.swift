import Foundation
import ImageIO
import CoreGraphics
// Reads paths on stdin, prints "dhash<TAB>w<TAB>h<TAB>path" (64-bit difference hash of a 9x8 gray thumbnail)
while let line = readLine() {
    let url = URL(fileURLWithPath: line)
    guard let src = CGImageSourceCreateWithURL(url as CFURL, nil),
          let props = CGImageSourceCopyPropertiesAtIndex(src, 0, nil) as? [CFString: Any],
          let thumb = CGImageSourceCreateThumbnailAtIndex(src, 0, [kCGImageSourceCreateThumbnailFromImageAlways: true, kCGImageSourceThumbnailMaxPixelSize: 128] as CFDictionary) else { continue }
    let w = props[kCGImagePropertyPixelWidth] as? Int ?? 0, h = props[kCGImagePropertyPixelHeight] as? Int ?? 0
    var px = [UInt8](repeating: 0, count: 72)
    let ctx = CGContext(data: &px, width: 9, height: 8, bitsPerComponent: 8, bytesPerRow: 9, space: CGColorSpaceCreateDeviceGray(), bitmapInfo: CGImageAlphaInfo.none.rawValue)!
    ctx.setFillColor(gray: 1, alpha: 1); ctx.fill(CGRect(x: 0, y: 0, width: 9, height: 8))
    ctx.interpolationQuality = .high
    ctx.draw(thumb, in: CGRect(x: 0, y: 0, width: 9, height: 8))
    var hsh: UInt64 = 0
    for y in 0..<8 { for x in 0..<8 { hsh <<= 1; if px[y*9+x] > px[y*9+x+1] { hsh |= 1 } } }
    print(String(format: "%016llx", hsh) + "\t\(w)\t\(h)\t" + line)
}
