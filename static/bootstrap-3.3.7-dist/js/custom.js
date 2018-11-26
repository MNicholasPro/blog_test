$(function(){
    function footerPosition(){
        $("footer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight,//网页正文全文高度
            winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
        if(!(contentHeight > winHeight)){
            //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
            $("footer").addClass("fixed-bottom");
        }
    }
    footerPosition();
    $(window).resize(footerPosition);
});

function deleteRecord(deleteId, type) {
    var address = "";
    if (type == 1){
        address = "/booksdata/delete-author/";
    }else if (type == 2){
        address = "/booksdata/delete-booktype/";
    }else if (type == 3){
        address = "/booksdata/delete-dept/";
    }else if (type == 4){
        address = "/booksdata/delete-publisher/";
    }
    $.getJSON(address + deleteId, {}, function (data) {
        if (data == 1){
            alert("删除成功！！！");
            location.reload();
        }
        else {
            alert("删除失败，请联系管理员！！！");
        }
    });
}

function changetoold(newId) {
    $.getJSON("/booksdata/change-books/" + newId, {}, function (data) {
        if (data == 1){
            alert("删除成功！！！");
            location.reload();
        }
        else {
            alert("删除失败，请联系管理员！！！");
        }
    });
}

function Assign_get_id(bookId) {
    // var bookId=$(assign).parents("tr").find("#get_id").text();
    window.bookId = bookId;
}

function borrowbook(bookId, type) {
    var dept_code = $("#dept_code").val();
    var borrow_item = $("#borrow_item").val();
    var borrow_start = $("#borrow_start").val();
    var borrow_end = $("#borrow_end").val();
    if (type == 1){
        $.post("/booksdata/borrow-books/", {"book_id":window.bookId,"dept_code":dept_code[0],"borrow_item":borrow_item,"borrow_start":borrow_start,"borrow_end":borrow_end}, function (data) {
            if (data == 1){
                alert("借阅成功！！！");
                location.reload();
            }
            else {
                alert("借阅失败，请联系管理员！！！");
            }
        });
    }else if(type == 2){
        $.getJSON("/booksdata/return-books/" + bookId, {}, function (data) {
            if (data == 1){
                alert("归还成功！！！");
                location.reload();
            }
            else if (data == 2){
                alert("请使用借阅人的账号进行归还操作，或者联系管理员，谢谢！！！");
            }
            else {
                alert("归还失败，请联系管理员！！！");
            }
        });
    }

}