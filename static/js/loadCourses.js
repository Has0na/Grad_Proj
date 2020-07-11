var app = document.getElementById('1stPr');
    app.innerHTML = '';
// 'Compiler Construction', 'Introduction to Computer Security', 'Web Programming', 'Computer Vision'
//     var subjects = {{ lst|safe }};

for (i = 0; i < subj1.length; i++) {
    var item = document.createElement('div');
    item.setAttribute('class', 'check_item');
    var checkbox = document.createElement('input');

            // Assigning the attributes         // to created checkbox
            checkbox.type = "checkbox";
            checkbox.name = "name";
            checkbox.value = subj1[i];
            checkbox.id = "id_" + subj1[i];
            checkbox.setAttribute('class', 'chekboxPr');

            // creating label for checkbox
            var label = document.createElement('label');
            // assigning attributes for         // the created label tag
            label.htmlFor = "id";
            // appending the created text to    // the created label tag
            label.appendChild(document.createTextNode(subj1[i]));
            item.appendChild(checkbox);
            item.appendChild(label);
            app.append(item)
}




 app = document.getElementById('2ndPr');

    app.innerHTML = '';

 subjects = ['Probability and Statistics', 'Computers and Ethics', 'Systems Analysis and Design', 'File Organization','Probability and Statistics', 'Computers and Ethics',
            'Systems Analysis and Design'];

for (i = 0; i < subjects.length; i++) {
    var item = document.createElement('div');
    item.setAttribute('class', 'check_item');
    var checkbox = document.createElement('input');

            // Assigning the attributes         // to created checkbox
            checkbox.type = "checkbox";
            checkbox.name = "name";
            checkbox.value = subjects[i];
            checkbox.id = "id_" + subjects[i];
            checkbox.setAttribute('class', 'chekboxPr');

            // creating label for checkbox
            var label = document.createElement('label');
            // assigning attributes for         // the created label tag
            label.htmlFor = "id";
            // appending the created text to    // the created label tag
            label.appendChild(document.createTextNode(subjects[i]));
            item.appendChild(checkbox);
            item.appendChild(label);
            app.append(item)
}

