const video = document.getElementById('webcam');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('capture');
const resultDiv = document.getElementById('result');

function countdownAndCapture() {
    resultDiv.textContent = '';
    let steps = ["Rock...", "Paper...", "Scissors...", "Shoot!"];
    let i = 0;

    function nextStep() {
        if (i < steps.length) {
            resultDiv.textContent = steps[i];
            i++;
            setTimeout(nextStep, i === steps.length ? 500 : 700);
        } else {
            captureAndSend();
        }
    }
    nextStep();
}

function captureAndSend() {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('image', blob, 'capture.png');
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(res => {
            if (!res.ok) {
                return res.json().then(data => { throw data; });
            }
            return res.json();
        })
        .then(data => {
            let resultColor = "text-yellow-400";
            if (data.result === "win") resultColor = "text-green-400";
            else if (data.result === "lose") resultColor = "text-red-400";
            else if (data.result === "tie") resultColor = "text-yellow-400";

            resultDiv.innerHTML = `
                <span class="block text-purple-300">You showed: ${data.user_sign.toUpperCase()}</span>
                <span class="block text-blue-300">Computer: ${data.computer_sign.toUpperCase()}</span>
                <span class="block font-bold ${resultColor}">Result: ${data.result.toUpperCase()}</span>
            `;
            captureBtn.textContent = "Try Again";
            captureBtn.disabled = false;
        })
        .catch(err => {
            resultDiv.innerHTML = `<span class="block text-red-400 font-bold">Error: ${err.error || "Could not get sign."}</span>`;
            captureBtn.textContent = "Try Again";
            captureBtn.disabled = false;
        });
    }, 'image/png');
}

captureBtn.addEventListener('click', () => {
    captureBtn.disabled = true;
    captureBtn.textContent = "Capturing...";
    countdownAndCapture();
});

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    })
    .catch(err => {
        resultDiv.textContent = "Error: Could not access webcam.";
    });