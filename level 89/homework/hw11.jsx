function App() {
  const numbers = [10, 20, 30];

  return (
    <div>
      {numbers.map((value, index) => (
        <p key={index}>
          Index: {index}, Value: {value}
        </p>
      ))}
    </div>
  );
}

export default App;