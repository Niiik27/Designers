const mainImage = document.getElementById('main-image');
const thumbnailsContainer = document.getElementById('thumbnails-container');

// Пути к изображениям (замените их на реальные пути или URL)
const imagePaths = ['path_to_image1.jpg', 'path_to_image2.jpg', 'path_to_image3.jpg', /* ...другие пути к изображениям... */];

// Создаем миниатюры программно на основе путей к изображениям
imagePaths.forEach((imagePath, index) => {
    const thumbnail = document.createElement('img');
    thumbnail.classList.add('thumbnail');
    thumbnail.src = imagePath;
    thumbnail.alt = `Миниатюра ${index + 1}`;

    // Добавляем обработчик события для каждой миниатюры
    thumbnail.addEventListener('click', () => {
        mainImage.src = imagePath;
        mainImage.alt = `Главная картинка ${index + 1}`;
    });

    thumbnailsContainer.appendChild(thumbnail);
});
