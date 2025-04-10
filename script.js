document.getElementById("uploadForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    
    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });
    
    const data = await res.json();
    document.getElementById("result").innerHTML = `
        <p><strong>Posture:</strong> ${data.posture}</p>
        <p><strong>Blinks per minute:</strong> ${data.blinks_per_minute}</p>
    `;
});
