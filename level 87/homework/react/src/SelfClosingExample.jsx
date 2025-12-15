function SelfClosingExample() {
  return (<>
    <img src="https://www.facebook.com/photo/?fbid=342479498535352&set=a.124602233656414" alt="GOA Logo" />
    <input type="text" placeholder="Enter Username" required/>
  </>)
}

export default SelfClosingExample;

{/*

კომპონენტი არის რეაქტის აპლიკაციის "სამშენებლო ბლოკი", ის არის ფუნცქია ანუ კოდის ბლოკი რომელიც შეგვიძლია ბევრჯერ გამოვიყენოთ და ის გვიბრუნებს ელემენტებს
return გვიბრუნებს იმ ელემენტებს რასაც გადავცემთ
JSX - javascript-ის სინტაქსის გაფართოება ანუ ბიბლიოთეკა რომელიც საშუალებას გვაძლევს HTML CSS JS დავწეროთ ერთ ფაილში
React-ში class მაგივრად className იმიტომ ვიყენებთ რომ class javascript-ში არის რეზერვირებული სიტყვა
მაგალითად onClick რომლის მნიშვნელობა არ შეიძლება იყოს სტრინგი, აუცილებლად უნდა იყოს ფუნქცია 

  */}