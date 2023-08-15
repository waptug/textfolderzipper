async function fetchFiles() {
    const response = await fetch("/list_files");
    const files = await response.json();

    const fileList = document.getElementById("fileList");
    const selectedFile = document.getElementById("selectedFile");

    for (const file of files) {
        const li = document.createElement("li");
        li.textContent = file;
        fileList.appendChild(li);

        const option = document.createElement("option");
        option.value = file;
        option.textContent = file;
        selectedFile.appendChild(option);
    }
}

async function buyFile() {
    const email = document.getElementById("email").value;
    const name = document.getElementById("name").value;
    const file = document.getElementById("selectedFile").value;

    const response = await fetch("/buy_file", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, name, file })
    });

    const result = await response.json();
    if (result.success) {
        alert("Payment successful! The ZIP file will be sent to your email shortly.");
    } else {
        alert("There was an error processing your payment.");
    }
}

fetchFiles();
