const fs = require('fs');

fs.readFile('./metro_2.json', 'utf8', function (err, metro) {
    metro = JSON.parse(metro);
    fs.readFile('./city_areas_3_with_coordinates.json', 'utf8', function (err, city) {
        city = JSON.parse(city);

        city.forEach(c => {
            c["地铁线路"] = metro[c["城市"]];
        });

        fs.writeFile('./data.json', JSON.stringify(city), function (err) {});
    });
});