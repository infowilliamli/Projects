// 1. deposit an amount of money
// 2. determine number of lines the user bets on
// 3. collect the bet amount
// 4. spin slot machine (3.5 build slot machine)
// 5. check if user won
// 6. give user the winnings (or take the bet)
// 7. play again

const prompt = require("prompt-sync")();

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    "@": 1,
    "#": 3,
    "%": 5,
    "$": 10
};

const SYMBOLS_VALUES = {
    "@": 5,
    "#": 4,
    "%": 3,
    "$": 2
};

const spin = () => {
    const symbols = [];

    for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)) {
        for (let i=0; i < count; i++) {
            symbols.push(symbol);
        }
    }

    const slotMachine = [];
    for (let i=0; i < COLS; i++) {
        slotMachine.push([]);
        const reel = [...symbols];
        for (let j=0; j < ROWS; j++) {
            const randomIndex = Math.floor(Math.random() * reel.length);
            const selectedSymbol = reel[randomIndex];
            slotMachine[i].push(selectedSymbol);
            reel.splice(randomIndex, 1);
        }
    }

    //console.log("Slots: ", slotMachine);
    return slotMachine;
};

const deposit = () => {
    while (true) {
        const depositAmount = prompt("Enter a deposit amount: ");
        const Deposit = parseFloat(depositAmount);

        if (isNaN(Deposit) || Deposit <= 0) {
            console.log("Invalid Deposit, please try again.");
        } else {
            console.log("You have deposited $" + Deposit);
            return Deposit;
        }
    }
};

const betLines = () => {
    while (true) {
        const bet = prompt("How many lines would you like to bet on? (1-3): ");
        const numberBet = parseInt(bet);

        if (isNaN(numberBet) || numberBet < 1 || numberBet > 3) {
            console.log("Invalid bet, please try again.");
        } else {
            console.log("You have bet on " + numberBet + " line(s)");
            return numberBet;
        }
    }
};

const betAmount = (balance, numLines) => {
    while (true) {
        const amount = prompt("How much would you like to bet per line? (balance: " + balance + "): ");
        const numberAmount = parseFloat(amount);

        if (isNaN(numberAmount) || numberAmount*numLines > balance || numberAmount <= 0) {
            console.log("Invalid bet, please try again.");
        } else {
            console.log("You have bet $" + numberAmount + " per line");
            return numberAmount;
        }
    }
};

const transpose = (reels) => {
    const rows = [];

    for (let i=0; i < ROWS; i++) {
        rows.push([]);
        for (let j=0; j < COLS; j++) {
            rows[i].push(reels[j][i]);
        }
    }

    //console.log("transposed slots: ", rows);
    return rows;
};

const printSlot = (reels) => {
    for (const reel of reels) {
        let reelString = "";
        for (const [i, symbol] of reel.entries()) {
            reelString += symbol;
            if (i != reel.length - 1) {
                reelString += " | ";
            }
        }

        console.log(reelString);
    }
}

const getWinnings = (reels, betPerReel, lines) => {
    let winnings = 0;

    for (let row=0; row < lines; row++) {
        const symbols = reels[row];
        let allSame = true;

        for (const symbol of symbols) {
            if (symbol != symbols[0]) {
                allSame = false;
                break;
            }
        }

        if (allSame) {
            winnings += betPerReel * SYMBOLS_VALUES[symbols[0]];
        }
    }

    return winnings;
}

const game = () => {
    let depositAmount = deposit();

    while (true) {
        const bet = betLines();
        const betPerReel = betAmount(depositAmount, bet);
        depositAmount -= bet * betPerReel;

        const spins = spin();
        const reels = transpose(spins);
        printSlot(reels);

        const winnings = getWinnings(reels, betPerReel, bet)
        depositAmount += winnings
        console.log("You have won $" + winnings.toString())

        if (depositAmount == 0) {
            console.log("Your balance is empty!");
            break;
        } else {
            console.log("Your remaining balance is: $" + depositAmount.toString())

            const playAgain = prompt("Do you wish to spin again? (y/n): ")
            if (playAgain != "y") break;
        }
        
    }
}

game();