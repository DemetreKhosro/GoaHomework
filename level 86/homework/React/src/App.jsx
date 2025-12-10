import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import SimpleGreeting from "./simplegreeting";
import MyInfo from "./myinfo";
import NumberList from "./numberslist";
import ImagesBlock from "./imagesblock";

function App() {
  return (
    <>
    {/*Task 1*/}
    <div>
      <SimpleGreeting/>
    </div>

    {/*Task 2*/}
    <div>
      <MyInfo/>
    </div>

    {/*Task 3*/}
    <div>
      <NumberList/>
    </div>

    {/*Task 4*/}
    <div>
      <ImagesBlock/>
    </div>
    </>
)};


export default App
