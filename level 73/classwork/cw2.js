// 2) შექმენით თარიღის ობიექტი, რომელშიც შეინახავთ 2023 წლის სექტემბერის 5 რიცხვს. ამისთვის გადაეცით date ობიექტის სტირნგის სახით თარიღი, კომენტარებით დაწერთ კიდევ როგორ შეიძლება date ობიექტს გადავცეთ თარიღი და თუ არ გადავცემთ არგუმენტს რა მოხდება. შექმნილი date ობიექტი შეინახეთ hireDate ცვლადში და ცალცალკე კონსოლში გამოიტანეთ წელი, თვე, რიცხვი, კვირის დღე, საათები, წუთები და წამები

const hireDate = new Date("2023-09-05");

console.log(hireDate.getFullYear());    
console.log(hireDate.getMonth() + 1);   
console.log(hireDate.getDate());        
console.log(hireDate.getDay());         
console.log(hireDate.getHours());       
console.log(hireDate.getMinutes());     
console.log(hireDate.getSeconds());

// date-ს რამდენიმენაირად შეგვიძლია გადავცეთ თარიღი
// სტრინგად  "2023-09-05"
// ინტეჯერებად 2023, 9, 5
// ცარიელი დავტოვოთ (ამჟამინდელი დრო)

console.log(Date());
