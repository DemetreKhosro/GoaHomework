class Triangle {
    constructor(a, b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
}

class AdvancedTriangle extends Triangle {
    perimeter() {
        return this.a + this.b + this.c;
    }
}

const tri = new AdvancedTriangle(3, 4, 5);
console.log(tri.perimeter());