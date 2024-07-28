const cells = document.querySelectorAll('.cell');
const message = document.querySelector('.message');
const board = Array.from(Array(9).keys());
const winningCombinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];
let currentPlayer = 'X';

const aiPlayer = 'O';
const humanPlayer = 'X';

function aiTurn(board) {
    // Your AI logic here to determine the best move
    // Replace this with your minimax implementation
    const randomIndex = Math.floor(Math.random() * board.length);
    return randomIndex;
}

function checkWin(player) {
    let plays = board.reduce((a, e, i) => (e === player) ? a.concat(i) : a, []);
    let gameWon = false;
    for (let [index, win] of winningCombinations.entries()) {
        if (win.every(elem => plays.indexOf(elem) > -1)) {
            gameWon = true;
            break;
        }
    }
    if (gameWon) {
        message.textContent = `${player} has won!`;
        return true;
    }
    return false;
}

function checkTie() {
    if (emptySquares().length === 0) {
        message.textContent = 'Tie!';
        return true;
    }
    return false;
}

function emptySquares() {
    return board.filter(s => typeof s === 'number');
}

function handleClick(e) {
    const cellIndex = this.getAttribute('data-cell-index');
    if (typeof board[cellIndex] === 'number') {
        updateBoard(this, cellIndex);
        if (!checkWin(currentPlayer)) {
            if (!checkTie()) {
                aiTurn(board);
            }
        }
    }
}

function updateBoard(cell, index) {
    board[index] = currentPlayer;
    cell.textContent = currentPlayer;
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

cells.forEach(cell => cell.addEventListener('click', handleClick));
