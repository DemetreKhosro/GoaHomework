class Player {
    constructor(name) {
        this.name = name;
    }
}

class GamePlayer extends Player {
    static playerCount = 0;

    constructor(name, level) {
        super(name);
        this.level = level;
        GamePlayer.playerCount++;
    }

    static resetPlayers() {
        GamePlayer.playerCount = 0;
    }
}

const p1 = new GamePlayer("Alice", 5);
const p2 = new GamePlayer("Bob", 3);

console.log(GamePlayer.playerCount);
GamePlayer.resetPlayers();
console.log(GamePlayer.playerCount);
