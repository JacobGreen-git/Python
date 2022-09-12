class Animal{
    constructor(name, species, region){
        this.name = name;
        this.species = species;
        this.region = region;
    }
}

let lion = new Animal("Lion","Cat", "Africa")

console.log(lion.name, lion.species, lion.region)