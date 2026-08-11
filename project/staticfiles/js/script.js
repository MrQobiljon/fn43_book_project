document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.querySelector("#searchInput");
    const books = document.querySelectorAll(".book-card");
    const categoryLinks = document.querySelectorAll(".category-link");

    // =========================
    // SEARCH
    // =========================

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchText = this.value.toLowerCase();

            let foundBooks = 0;

            books.forEach(function (book) {

                const title = book
                    .querySelector(".book-title")
                    .textContent
                    .toLowerCase();

                const category = book
                    .querySelector(".category")
                    .textContent
                    .toLowerCase();

                if (
                    title.includes(searchText) ||
                    category.includes(searchText)
                ) {
                    book.style.display = "block";
                    foundBooks++;
                } else {
                    book.style.display = "none";
                }

            });

            showNoResults(foundBooks);

        });

    }


    // =========================
    // CATEGORY FILTER
    // =========================

    categoryLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            event.preventDefault();

            const selectedCategory = this.dataset.category;

            categoryLinks.forEach(function (item) {
                item.classList.remove("active");
            });

            this.classList.add("active");

            let foundBooks = 0;

            books.forEach(function (book) {

                const bookCategory =
                    book.dataset.category;

                if (
                    selectedCategory === "all" ||
                    bookCategory === selectedCategory
                ) {

                    book.style.display = "block";
                    foundBooks++;

                } else {

                    book.style.display = "none";

                }

            });

            // Search inputni tozalash
            if (searchInput) {
                searchInput.value = "";
            }

            showNoResults(foundBooks);

        });

    });


    // =========================
    // NO RESULTS MESSAGE
    // =========================

    function showNoResults(count) {

        let message = document.querySelector(".no-results");

        if (count === 0) {

            if (!message) {

                message = document.createElement("div");

                message.className = "no-results";

                message.textContent =
                    "Kitob topilmadi.";

                document
                    .querySelector(".books-container")
                    .appendChild(message);
            }

        } else {

            if (message) {
                message.remove();
            }

        }

    }

});