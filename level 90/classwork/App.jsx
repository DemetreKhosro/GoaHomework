import MyComponent from "./Component";

function App() {
  return (
    <>
      <MyComponent />
      {/* 
        react-dom იმიტომ ვიყენებთ რომ დავაკავშიროთ react ბრაუზერის dom-თან
        createRoot() ქმნის react-ის root-ს ანუ DOM-ის მთავარ წერტილს
        render იღებს react ან კომპონენტს ან jsx-ს და გარდაქმნის HTML ელემენტად
      */}
    </>
  );
}

export default App;