INSERT INTO users (email, password, first_name, last_name, image_url)
VALUES
(
    'test@gmail.com',
    'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f',
    'Test',
    'Testowy',
    'https://link_to_image.com'
),
(
    'other@wp.pl',
    'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79',
    'Anonimowy',
    'Anonim',
    'https://link_to_image2.com'
);

INSERT INTO links (user_id, platform, url, created)
VALUES
(1, 'GitHub', 'https://github.com/TestTestowy', '2025-03-14 00:00:00'),
(2, 'LinkedIn', 'https://www.linkedin.com/in/anonimowy-anonim', '2025-03-14 00:00:00');
