function UsernameCheck() {
  const username = 'Demetre'
  return (<>
    <div>
      {username ? (<p>Hello {username}</p>) : (<p>hello world!</p>)}
    </div>
  </>)
}