class Student {
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }
}

class RankedStudent extends Student {
    constructor(name, grade, rank) {
        super(name, grade);
        this.rank = rank;
    }

    static sortStudents(students) {
        return students.sort((a, b) => a.rank - b.rank);
    }
}