var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
var data = imgData.data;


bline(60, 100, 400, 450);
ctx.putImageData(imgData, 0, 0);

//console.log(1)

function setPixel(x, y) {
    var n = (y * canvas.width + x) * 4;
    data[n] = 0;
    data[n + 1] = 0;
    data[n + 2] = 255;
    data[n + 3] = 255;
}

// Refer to: http://rosettacode.org/wiki/Bitmap/Bresenham's_line_algorithm#JavaScript
function bline(x0, y0, x1, y1) {
    var dx = Math.abs(x1 - x0),
        sx = x0 < x1 ? 1 : -1;
    var dy = Math.abs(y1 - y0),
        sy = y0 < y1 ? 1 : -1;
    var err = (dx > dy ? dx : -dy) / 2;
    while (true) {
        setPixel(x0, y0);
        if (x0 === x1 && y0 === y1) break;
        var e2 = err;
        if (e2 > -dx) {
            err -= dy;
            x0 += sx;
        }
        if (e2 < dy) {
            err += dx;
            y0 += sy;
        }
    }
}