function toggleText(postId) {
    const content = document.getElementById(`post-content-${postId}`);
    const btn = document.getElementById(`toggle-btn-${postId}`);

    if (content.classList.contains("expanded")) {
        content.classList.remove("expanded");
        btn.innerHTML = "See more ▼";
    } else {
        content.classList.add("expanded");
        btn.innerHTML = "See less ▲";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const texts = document.querySelectorAll('.collapsible-text');
    texts.forEach(text => {
        // If the scrollHeight is less than or equal to the visible height, hide the button
        if (text.scrollHeight <= text.offsetHeight) {
            const id = text.id.split('-').pop();
            const btn = document.getElementById(`toggle-btn-${id}`);
            if (btn) btn.style.display = 'none';
        }
    });
});