// pdfdiff A.pdf B.pdf: per page, the share of pixels that differ (each page rendered at 60 dpi with PDFKit). a11y_files.py
// fixclass builds it once into ~/Library/Caches/CanvasPreview/pdfdiff and compares every page of a fixed slide PDF
// with the same export of the unchanged deck.
import PDFKit
import AppKit
func bitmap(_ p: PDFPage) -> [UInt8] {
    let b = p.bounds(for: .mediaBox); let s: CGFloat = 60.0/72.0
    let w = Int(b.width*s), h = Int(b.height*s)
    var px = [UInt8](repeating: 255, count: w*h*4)
    let cs = CGColorSpaceCreateDeviceRGB()
    px.withUnsafeMutableBytes { buf in
        let ctx = CGContext(data: buf.baseAddress, width: w, height: h, bitsPerComponent: 8, bytesPerRow: w*4, space: cs, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
        ctx.setFillColor(.white); ctx.fill(CGRect(x:0,y:0,width:w,height:h)); ctx.scaleBy(x: s, y: s)
        p.draw(with: .mediaBox, to: ctx)
    }
    return px
}
let a = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1]))!, b = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[2]))!
if a.pageCount != b.pageCount { print("PAGES \(a.pageCount) vs \(b.pageCount)") }
var worst = 0.0; var bad: [String] = []
for i in 0..<min(a.pageCount, b.pageCount) {
    let x = bitmap(a.page(at: i)!), y = bitmap(b.page(at: i)!)
    if x.count != y.count { bad.append("\(i+1):size"); continue }
    var d = 0; var j = 0
    while j < x.count { if abs(Int(x[j])-Int(y[j])) > 40 || abs(Int(x[j+1])-Int(y[j+1])) > 40 || abs(Int(x[j+2])-Int(y[j+2])) > 40 { d += 1 }; j += 4 }
    let f = Double(d) / Double(x.count/4); worst = max(worst, f)
    if f > 0.002 { bad.append(String(format: "%d:%.2f%%", i+1, f*100)) }
}
print(String(format: "worst %.3f%%", worst*100), bad.isEmpty ? "SAME" : "DIFF " + bad.joined(separator: " "))
