document.addEventListener('DOMContentLoaded', function() {
    // Load content from JSON file
    fetch('content.json')
        .then(response => response.json())
        .then(data => {
            // Populate content
            populateContent(data);
        })
        .catch(error => console.error('Error loading content:', error));

    function populateContent(content) {
        // Set page title
        document.title = content.siteTitle;
        document.querySelector('.logo').textContent = content.siteTitle;

        // Populate navigation
        const navUl = document.querySelector('nav ul');
        content.navigation.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `<a href="${item.link}">${item.label}</a>`;
            navUl.appendChild(li);
        });

        addSmoothScrolling();

        // Set hero content
        document.querySelector('#hero h1').textContent = content.hero.title;
        document.querySelector('#hero .date').textContent = content.hero.date;
        document.querySelector('#hero').style.backgroundImage = `url(${content.hero.backgroundImages})`;

        // Populate speakers
        /*const speakerGrid = document.querySelector('.speaker-grid');
        content.speakers.list.forEach(speaker => {
            const speakerCard = document.createElement('div');
            speakerCard.className = 'speaker-card';
            speakerCard.innerHTML = `
                <img src="${speaker.photo}" alt="${speaker.name}">
                <h3>${speaker.name}</h3>
                <p class="title">${speaker.title}</p>
                <div class="description">
                    <p>${speaker.description}</p>
                </div>
            `;
            speakerGrid.appendChild(speakerCard);
        });*/

        // Populate Documents
        /*const documentsContent = document.querySelector('.documents-content');
        content.documents.items.forEach(item => {
            const documentItem = document.createElement('div');
            documentItem.className = 'documents-item';
            documentItem.innerHTML = `
                <a href="./public/documents/${item.no}.html" target="_blank">${item.titles}</a> <p class="author">- ${item.author}</p>
            `;
            documentsContent.appendChild(documentItem);
        });*/

        // Populate Documents
        const documentsContent = document.querySelector('.documents-content');
        content.documents.items.forEach(item => {
            const documentItem = document.createElement('a');
            documentItem.href = `./public/documents/${item.no}.html`;
            documentItem.target = "_blank";
            documentItem.innerHTML = `
                <div class="documents-item"><h3>${item.titles}</h3><p class="author">- ${item.author}</p></div> 
            `;
            documentsContent.appendChild(documentItem);
        });

        // Set footer content
        /*document.querySelector('.organizers h3').textContent = content.footer.organizer.title;
        document.querySelector('.organizers img').src = content.footer.organizer.image;
        document.querySelector('.co-organizers h3').textContent = content.footer.coOrganizer.title;
        document.querySelector('.co-organizers img').src = content.footer.coOrganizer.image;
        document.querySelector('.sponsors h3').textContent = content.footer.sponsor.title;
        document.querySelector('.sponsors img').src = content.footer.sponsor.image;*/
        document.querySelector('.contact h3').textContent = content.footer.contact.title;
        document.querySelector('.contact p:nth-child(2)').textContent = `Phone: ${content.footer.contact.phone}`;
        document.querySelector('.contact p:nth-child(3)').textContent = `Address: ${content.footer.contact.address}`;
    }

    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navUl = document.querySelector('nav ul');

    menuToggle.addEventListener('click', function() {
        navUl.classList.toggle('show');
    });

    function addSmoothScrolling() {
        document.querySelector('nav').addEventListener('click', function(e) {
            if (e.target.tagName === 'A' && e.target.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = e.target.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    const headerOffset = 100;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    }

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrollPosition = window.pageYOffset;
        document.querySelector('#hero').style.backgroundPositionY = scrollPosition * 0.7 + 'px';
    });
});