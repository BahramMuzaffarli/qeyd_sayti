<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>Qeyd Saytı - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f8fb;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #004080;
            text-align: center;
        }
        p {
            line-height: 1.6;
            font-size: 16px;
        }
        ul {
            margin-left: 20px;
        }
        code {
            background-color: #e1f0ff;
            padding: 2px 6px;
            border-radius: 4px;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Qeyd Saytı</h1>
        <p>
            Bu layihə sadə bir web tətbiqdir, istifadəçilərin ad, soyad və qeydlərini daxil edə biləcəyi bir platforma təqdim edir.
        </p>

        <h2>Əsas Xüsusiyyətlər</h2>
        <ul>
            <li>İstifadəçi login funksiyası (sadə nümunə)</li>
            <li>Ad, soyad və qeyd əlavə etmək imkanı</li>
            <li>Qeydlərin cədvəl şəklində göstərilməsi</li>
            <li>Logout funksiyası ilə əsas səhifəyə qayıtma</li>
            <li>Gözəl, açıq mavi və dark blue dizayn</li>
        </ul>

        <h2>Quraşdırma</h2>
        <p>
            Layihəni öz maşınınızda işlətmək üçün:
        </p>
        <pre>
git clone <a href="https://github.com/BahramMuzaffarli/qeyd_sayti.git">https://github.com/BahramMuzaffarli/qeyd_sayti.git</a>
cd qeyd_sayti
python -m venv venv
venv\Scripts\activate  &nbsp;# Windows üçün
pip install -r requirements.txt
python manage.py runserver
        </pre>

        <h2>İstifadə</h2>
        <p>
            1. Login səhifəsinə daxil olun.<br>
            2. İstifadəçi adı daxil edin və <code>Submit</code> edin.<br>
            3. Qeyd əlavə etmək üçün formu doldurun və <code>Save</code> düyməsinə basın.<br>
            4. Logout düyməsi ilə əsas səhifəyə qayıdın.
        </p>

        <h2>Əlaqə</h2>
        <p>
            Layihə müəllifi: <strong>Bahram Muzaffarli</strong><br>
            <a href="https://github.com/BahramMuzaffarli">GitHub Profil</a>
        </p>
    </div>
</body>
</html>
