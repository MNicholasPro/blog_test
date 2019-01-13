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
    var r = confirm('请确定是否删除，选择"确认/OK"直接删除，选择"取消/Cancle"取消删除！！！!');
    var address = "";
    if (type == 1){
        address = "/booksdata/delete-author/";
    }else if (type == 2){
        address = "/booksdata/delete-booktype/";
    }else if (type = 3){
        address = "/booksdata/delete-dept/";
    }else if (type == 4){
        address = "/booksdata/delete-publisher/";
    }
    if (r == true ){
        $.getJSON(address + deleteId, {}, function (data) {
            if (data == 1){
                toastr.options.positionClass = 'toast-center-center';
                toastr.success("已经删除！！！");
                setTimeout(function(){location.reload();},3000);
            }
            else {
                toastr.options.positionClass = 'toast-center-center';
                toastr.error("删除失败，请联系管理员！！！");
            }
        });
    }else {
        toastr.options.positionClass = 'toast-center-center';
        toastr.success("已经取消！！！");
    }
}

function changetoold(newId, type) {
    var r = confirm('请确定是否删除，选择"确认/OK"直接删除，选择"取消/Cancle"取消删除！！！!');
    var address = "";
    if (type == 1){
        address = "/booksdata/change-books/";
    }else if (type == 2){
        address = "/booksdata/delete-wish-book/";
    }else if (type == 3){
        address = "/booksdata/delete-book-thoughts/";
    }
    if(r == true) {
        $.getJSON(address + newId, {}, function (data) {
            if (data == 1) {
                toastr.options.positionClass = 'toast-center-center';
                toastr.success("已经删除！！！");
                setTimeout(function () {
                    location.reload();
                }, 3000);
            }
            else {
                toastr.options.positionClass = 'toast-center-center';
                toastr.error("删除失败，请联系管理员！！！");
            }
        });
    }else {
        toastr.options.positionClass = 'toast-center-center';
        toastr.success("已经取消！！！");
    }
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
    if (type === 1){
        $.post("/booksdata/borrow-books/", {"book_id":window.bookId,"dept_code":dept_code[0],"borrow_item":borrow_item,"borrow_start":borrow_start,"borrow_end":borrow_end}, function (data) {
            if (data == 1){
                toastr.options.positionClass = 'toast-center-center';
                toastr.success("借阅成功！！！");
                setTimeout(function(){location.reload();},3000);
            }
            else {
                toastr.options.positionClass = 'toast-center-center';
                toastr.error("借阅失败，请联系管理员！！！");
            }
        });
    }else if(type == 2){
        $.getJSON("/booksdata/return-books/" + bookId, {}, function (data) {
            if (data == 1){
                toastr.options.positionClass = 'toast-center-center';
                toastr.success("归还成功！！！");
                setTimeout(function(){location.reload();},3000);
            }
            else if (data == 2){
                toastr.options.positionClass = 'toast-center-center';
                toastr.error("请使用借阅人的账号进行归还操作，或者联系管理员，谢谢！！！");
            }
            else {
                toastr.options.positionClass = 'toast-center-center';
                toastr.error("归还失败，请联系管理员！！！");
            }
        });
    }
}

function addReply(bookthoughtsid) {
    var b_replycontent = $("#b-ReplyContent").val();
    $.post('/booksdata/add-book-thoughts-reply/',{"bookthoughtsid":bookthoughtsid,"b_replycontent":b_replycontent},function(data){
        if(data=='1')
         {
             toastr.options.positionClass = 'toast-center-center';
             toastr.success("留言成功,感谢！！！");location.reload();
         }
         else
             toastr.options.positionClass = 'toast-center-center';
             toastr.error("未能成功留言，请联系管理员！！！");
    });
}

//重写confirm方法，去掉地址显示
window.confirm = function(name){
    var iframe = document.createElement("IFRAME");
    iframe.style.display="none";
    iframe.setAttribute("src", 'data:text/plain,');
    document.documentElement.appendChild(iframe);
    var result = window.frames[0].window.confirm(name);
    iframe.parentNode.removeChild(iframe);
    return result;
};

/**获取点赞数量**/
function agreeBook(wishBookId, agreeCount) {
    var agreeCountTotal = agreeCount + 1;
    $.post("/booksdata/update-wish-count/", {"wishBookId":wishBookId,"agreeCount":agreeCountTotal}, function (data) {
        if (data == 1){
            toastr.options.positionClass = 'toast-center-center';
            toastr.success("点赞成功,感谢！！！");
            setTimeout(function(){location.reload();},2000);
        }else if (data == 0){
            toastr.options.positionClass = 'toast-center-center';
            toastr.error("点赞失败，请联系管理员！！！");
        }else if(data == 3){
            toastr.options.positionClass = 'toast-center-center';
            toastr.warning("请勿重复点赞，谢谢！！！");
        }
    });
}