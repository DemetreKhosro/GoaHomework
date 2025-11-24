class Bike {
    constructor(speed) {
        this.speed = speed;
    }
}

class SpeedBike extends Bike {
    increaseSpeed(amount) {
        this.speed += amount;
    }
}

const sb = new SpeedBike(20);
sb.increaseSpeed(15);
console.log(sb.speed);
