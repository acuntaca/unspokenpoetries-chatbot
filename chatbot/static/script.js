function kirimPesan() {

    const input = document.getElementById("pesan");
    const chatBox = document.getElementById("chat-box");

    const pesan = input.value.trim();

    // Kalau input kosong
    if (pesan === "") {
        return;
    }

    // Kalau user mengetik "clear"
    if (pesan.toLowerCase() === "clear") {
        chatBox.innerHTML = "";
        input.value = "";
        return;
    }

    // Tampilkan pesan user
    chatBox.innerHTML += `
        <div class="user-message">${pesan}</div>
    `;

    // Kosongkan input
    input.value = "";

    // Scroll ke bawah
    chatBox.scrollTop = chatBox.scrollHeight;

    // Kirim ke Flask
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            pesan: pesan
        })
    })
    .then(response => response.json())
    .then(data => {

        // Tampilkan balasan bot
        chatBox.innerHTML += `
            <div class="bot-message">${data.balasan}</div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

// ===============================
// Tekan Enter untuk mengirim pesan
// ===============================
const inputPesan = document.getElementById("pesan");

inputPesan.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        kirimPesan();
    }
});