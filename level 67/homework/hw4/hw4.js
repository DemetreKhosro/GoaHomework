let playerScore = 0
let computerScore = 0

const playerScoreEl = document.getElementById("playerScore")
const computerScoreEl = document.getElementById("computerScore")
const computerChoiceEl = document.getElementById("computerChoice")
const resultBtn = document.getElementById("resultBtn")

const choices = ["rock", "paper", "scissors"]

function getComputerChoice() {
    return choices[Math.floor(Math.random() * choices.length)]
}

document.querySelectorAll(".choice").forEach(choice => {
    choice.onclick = () => {
        const playerChoice = choice.dataset.choice.toLowerCase()
        const computerChoice = getComputerChoice()
        computerChoiceEl.textContent = "Computer chose: " + computerChoice

        if (playerChoice === computerChoice) {
            resultBtn.textContent = "It's a draw!"
        } else if (
            (playerChoice === "rock" && computerChoice === "scissors") ||
            (playerChoice === "paper" && computerChoice === "rock") ||
            (playerChoice === "scissors" && computerChoice === "paper")
        ) {
            resultBtn.textContent = "You win!"
            playerScore++
        } else {
            resultBtn.textContent = "Computer wins!"
            computerScore++
        }

        playerScoreEl.textContent = "Your Score: " + playerScore
        computerScoreEl.textContent = "Computer Score: " + computerScore
    }
})

resultBtn.onclick = () => {
    playerScore = 0
    computerScore = 0
    playerScoreEl.textContent = "Your Score: 0"
    computerScoreEl.textContent = "Computer Score: 0"
    computerChoiceEl.textContent = ""
    resultBtn.textContent = "Start Game"
}