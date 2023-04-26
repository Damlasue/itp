let result = Number(prompt("pick the size of your chessboard from 8-8"));
let pattern1 = " " + "#"; 
let pattern2 = "#" + " "; 
let gridWidth = 4;

function getGrid(gridWidth) {
let output1 = pattern1.repeat(gridWidth) + '\n';
let output2 = pattern2.repeat(gridWidth)+ '\n';
let output3 = output1 + output2;

    let result = output3.repeat(gridWidth);

console.log(result);
}

getGrid(gridWidth);