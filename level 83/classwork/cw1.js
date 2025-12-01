const newMap = new Map([
    ['name', 'John'],
    ['age', 30],
    ['city', 'New York']
]);


console.log(newMap.get("name"));  
console.log(newMap.has("age"));     

newMap.set("job", "Developer");     
newMap.delete("city");             

console.log(newMap.keys());        
console.log(newMap.values());        
console.log(newMap.entries());       

newMap.clear();                      
console.log(newMap);

// მაგონებს dictionary-ს რადგან ის ინახავს key-value წყვილებსc