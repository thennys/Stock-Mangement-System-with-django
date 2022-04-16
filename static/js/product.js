$(document).ready(function () {
    function fetch_products_list() {
        $.ajax({
            url: $("#data_table").attr("data-url"),
            method: "get",
            success: function (response) {
                $("#data_table").html(response.html);
            }
        })
    }

    fetch_products_list();

    // $(document).on("click", "#btn-delete", function () {
    //     $("#removeBrandModal").modal("show");
    // });

    // $(document).on("click", "#btn-yes-delete", function () {
    //     $.ajax({
    //         url: $("#btn-delete").attr("data-url"),
    //         type: "delete",
    //         success: function (response) {
    //             $("#categoriesTable").html(response.html);
    //             $("#removeCategoryModal").modal("hide");
    //         }
    //
    //     })
    // })
    //
    // // $(document).on("click", "#btn-delete", function () {
    // //     $("#removeBrandModal").modal("show");
    // // });
    //

    $("#btn-add-product").click(function () {
        $.ajax({
            url: $("#btn-add-product").attr("data-url"),
            type: "get",
            dataType: "json",
            success: function (response) {
                $("#addProductModal .modal-body").html(response.html);
                $("#addProductModal").modal("show");
            }

        })
    })


    $(document).on("click", "#addProductBtn", function () {
        if ($(".create-form").attr("categoryName") == '') {
            null
        }
        else {
            $.ajax({
                url: $("#btn-add-product").attr("data-url"),
                type: "post",
                dataType: "json",
                data: $(".create-form").serialize(),
                success: function (response) {
                    $("#data_table").html(response.html);
                    $("#addCategoryModal").modal("hide");
                }

            })
        }
    })
    // //
    // // $(document).on("click", "#btn-update", function () {
    // //     $.ajax({
    // //         url: $("#btn-update").attr("data-url"),
    // //         type: "get",
    // //         success: function (response) {
    // //             $("#editBrandModal .modal-body").html(response.html);
    // //             $("#editBrandModal").modal("show");
    // //         }
    // //
    // //     })
    // // })
    // //
    // // $(document).on("click", "#updateBrandBtn", function () {
    // //     $.ajax({
    // //         url: $("#updateBrandBtn").attr("data-url"),
    // //         type: "post",
    // //         dataType: "json",
    // //         data: $(".update-form").serialize(),
    // //         success: function (response) {
    // //             $("#brandTable").html(response.html);
    // //             $("#editBrandModal").modal("hide");
    // //         }
    // //
    // //     })
    // // })
});

