function runEmotionDetection() {
    const text = document.getElementById("textToAnalyze").value;

    if (!text) {
        alert("Please enter some text for analysis.");
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.readyState === 4 && this.status !== 200) {
            document.getElementById("system_response").innerHTML = "Error occurred while analyzing text.";
        }
    };

    xhttp.open("GET", `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`, true);
    xhttp.send();
}