// Validasi input sebelum dikirim
function validateForm() {
    const a = document.getElementById("team_a").value;
    const b = document.getElementById("team_b").value;

    if (a === "" || b === "") {
        alert("Skor kedua tim harus diisi!");
        return false;
    }

    if (a < 0 || b < 0) {
        alert("Skor tidak boleh negatif!");
        return false;
    }

    return true;
}

// Animasi pemenang pada halaman result
function animateWinner() {
    const el = document.getElementById("winner_text");
    if (!el) return;

    el.style.transform = "scale(1.2)";
    el.style.transition = "0.3s";
    setTimeout(() => {
        el.style.transform = "scale(1)";
    }, 300);
}

window.onload = animateWinner;