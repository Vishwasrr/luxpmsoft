const { spawn } = require('child_process');

// const childPython = spawn('py', ['--version']);
const childPython = spawn('python', ['question_1.py']);


childPython.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
});

// childPython.stderr.on('data', (data) => {
//     console.log(`stderr: ${data}`);
// });

// childPython.on('close', (code) => {
//     console.log(`child process exited with code ${code}`);
// });