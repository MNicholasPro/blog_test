/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    // // 界面语言，默认为 'en'
    // config.language = 'zh-cn';
    // config.image_previewText=' ';
    // config.filebrowserImageUploadUrl= "/upload-image/";
    // config.removeDialogTabs = 'image:advanced;image:Link';//隐藏超链接与高级选项

    config.language = 'zh-cn';
    config.uiColor = '';
    config.extraPlugins = 'image';
    config.filebrowserUploadUrl = '/upload-image/';
    config.toolbar = [
        { name: 'document', items: ['Source', '-', 'Preview', 'Print', '-'] },
        { name: 'clipboard', items: ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'] },
        { name: 'editing', items: ['Find', 'Replace', '-', 'Styles'] },
        '/',
        { name: 'basicstyles', items: ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat'] },
        { name: 'paragraph', items: ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'] },
        { name: 'links', items: ['Link', 'Unlink'] },
        { name: 'insert', items: ['Image', 'Flash', 'Table'] },
        { name: 'tools', items: ['ShowBlocks'] }
    ];
    config.removeDialogTabs = 'image:advanced;image:Link';//隐藏超链接与高级选项
    config.toolbarCanCollapse = true;
    config.image_previewText=' ';

};
