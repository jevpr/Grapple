import ClassicEditor from './ckeditor.js';

const editorConfig = {
    toolbar: {
        items: [
            'sourceEditing', 'showBlocks', 'findAndReplace', 'textPartLanguage', '|',
            'heading', 'style', '|', 'fontSize', 'fontFamily', 'fontColor',
            'fontBackgroundColor', '|', 'bold', 'italic', 'underline',
            'strikethrough', 'subscript', 'superscript', 'code', 'removeFormat', '|',
            'specialCharacters', 'horizontalLine', 'link', 'bookmark', 'insertImage',
            'insertImageViaUrl', 'mediaEmbed', 'insertTable', 'highlight', 'blockQuote',
            'codeBlock', 'htmlEmbed', '|', 'alignment', '|', 'bulletedList',
            'numberedList', 'todoList', 'outdent', 'indent'
        ],
        shouldNotGroupWhenFull: false
    },
    placeholder: "Type your lesson content here!",
    fontFamily: {
        supportAllValues: true
    },
    fontSize: {
        options: [10, 12, 14, 'default', 18, 20, 22],
        supportAllValues: true
    },
    heading: {
        options: [
            { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
            { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
            { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
            { model: 'heading3', view: 'h3', title: 'Heading 3', class: 'ck-heading_heading3' },
            { model: 'heading4', view: 'h4', title: 'Heading 4', class: 'ck-heading_heading4' },
            { model: 'heading5', view: 'h5', title: 'Heading 5', class: 'ck-heading_heading5' },
            { model: 'heading6', view: 'h6', title: 'Heading 6', class: 'ck-heading_heading6' }
        ]
    },
    list: {
        properties: {
            styles: true,
            startIndex: true,
            reversed: true
        }
    },
    menuBar: {
        isVisible: true
    },
    table: {
        contentToolbar: ['tableColumn', 'tableRow', 'mergeTableCells', 'tableProperties', 'tableCellProperties']
    }
};

// ✅ Initialize CKEditor and save content into Django form field
ClassicEditor
    .create(document.querySelector('#editor'), editorConfig)
    .then(editor => {
        // ✅ Capture CKEditor content and put it inside a hidden textarea
        document.querySelector('form').addEventListener('submit', function () {
            const contentField = document.createElement('textarea');
            contentField.name = 'content';
            contentField.style.display = 'none';
            contentField.value = editor.getData();
            this.appendChild(contentField);
        });
    })
    .catch(error => console.error(error));
