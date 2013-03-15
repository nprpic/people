/* Bootstrap style pagination control */
$.extend( $.fn.dataTableExt.oPagination, {
    "bootstrap": {
        "fnInit": function( oSettings, nPaging, fnDraw ) {
            var oLang = oSettings.oLanguage.oPaginate;
            var fnClickHandler = function ( e ) {
                e.preventDefault();
                if ( oSettings.oApi._fnPageChange(oSettings, e.data.action) ) {
                    fnDraw( oSettings );
                }
            };

            $(nPaging).addClass('pagination').append(
                '<ul>'+
                    '<li class="prev disabled"><a href="#">&larr; '+oLang.sPrevious+'</a></li>'+
                    '<li class="next disabled"><a href="#">'+oLang.sNext+' &rarr; </a></li>'+
                '</ul>'+
            );
            var els = $('a', nPaging);
            $(els[0]).bind( 'click.DT', { action: "first" }, fnClickHandler );
            $(els[1]).bind( 'click.DT', { action: "previous" }, fnClickHandler );
            $(els[2]).bind( 'click.DT', { action: "next" }, fnClickHandler );
            $(els[3]).bind( 'click.DT', { action: "last" }, fnClickHandler );
        },

        "fnUpdate": function ( oSettings, fnDraw ) {
            var iListLength = 5;
            var oPaging = oSettings.oInstance.fnPagingInfo();
            var an = oSettings.aanFeatures.p;
            var i, j, sClass, iStart, iEnd, iHalf=Math.floor(iListLength/2);

            if ( oPaging.iTotalPages < iListLength) {
                iStart = 1;
                iEnd = oPaging.iTotalPages;
            }
            else if ( oPaging.iPage <= iHalf ) {
                iStart = 1;
                iEnd = iListLength;
            } else if ( oPaging.iPage >= (oPaging.iTotalPages-iHalf) ) {
                iStart = oPaging.iTotalPages - iListLength + 1;
                iEnd = oPaging.iTotalPages;
            } else {
                iStart = oPaging.iPage - iHalf + 1;
                iEnd = iStart + iListLength - 1;
            }

            if (oPaging.iTotalPages < 6) {
                $("a.first, a.last").hide();
            }
            else {
                $("a.first, a.last").show();
            }

            for ( i=0, iLen=an.length ; i<iLen ; i++ ) {
                // Remove the middle elements
                $('li:gt(0)', an[i]).filter(':not(:last)').remove();

                // Add the new list items and their event handlers
                for ( j=iStart ; j<=iEnd ; j++ ) {
                    sClass = (j==oPaging.iPage+1) ? 'class="active"' : '';
                    $('<li '+sClass+'><a href="#">'+j+'</a></li>')
                        .insertBefore( $('li:last', an[i])[0] )
                        .bind('click', function (e) {
                            e.preventDefault();
                            oSettings._iDisplayStart = (parseInt($('a', this).text(),10)-1) * oPaging.iLength;
                            fnDraw( oSettings );
                        } );
                }

                // Add / remove disabled classes from the static elements
                if ( oPaging.iPage === 0 ) {
                    $('li:first', an[i]).addClass('disabled');
                } else {
                    $('li:first', an[i]).removeClass('disabled');
                }

                if ( oPaging.iPage === oPaging.iTotalPages-1 || oPaging.iTotalPages === 0 ) {
                    $('li:last', an[i]).addClass('disabled');
                } else {
                    $('li:last', an[i]).removeClass('disabled');
                }
            }
        }
    }
} );

function createTable(id, fields, iDisplayLength, aaSorting, aaData, columnFilter, bStateSave){
    var _bStateSave = (bStateSave == false) ? false : true;
    var oTable = $(id).dataTable( {
        "bJQueryUI": true,
        "oLanguage": {
            "sProcessing": "Molimo pri&#269;ekajte...",
            "sLengthMenu": "Prikazano _MENU_ zapisa",
            "sZeroRecords": "Nema zapisa za prikaz",
            "sEmptyTable": "Nema zapisa za prikaz",
            "sLoadingRecords": "U&#269;itavam...",
            "sInfo": "Prikazano _START_ do _END_ od ukupno _TOTAL_ zapisa",
            "sInfoEmpty": "Prikazano 0 do 0 od ukupno 0 zapisa",
            "sInfoFiltered": "(filtrirano od ukupno _MAX_ zapisa)",
            "sInfoPostFix": "",
            "sSearch": "Filtriraj",
            "sUrl": "",
            "oPaginate": {
                "sFirst":    "Prva",
                "sPrevious": "Prethodna",
                "sNext":     "Sljede&#263;a",
                "sLast":     "Posljednja"
            }
        },
        "fnRowCallback": function(nRow, aData, iDisplayIndex, iDisplayIndexFull){
            $(nRow).attr('data-id', aData[aData.length-1]);
            return nRow;
        },
        "sDom": '<"top"p>t<"bottom"p>',
        "sPaginationType": "bootstrap",

        "iDisplayLength": iDisplayLength,
        "bStateSave": _bStateSave,
        "aoColumns": fields,
        "bInfo": false,
        "bPaginate": true,
        "aaSorting": aaSorting,

        "aaData": aaData,
    });

    if (columnFilter)
    {
        oTable.columnFilter(columnFilter);
    }
    $(id + " thead a.search_adv_show").click(function(){
        showAndClearAdvSearch(this, id);
    })

    $(id + " thead a.search_adv_close").click(function(){
        closeAndClearAdvSearch(id);
    })

    return oTable;
}

// Zatvaranje naprednog pretrazivanja
function closeAndClearAdvSearch(id){
    $(id + ' .filter_header').hide();

    return false;
}

function showAndClearAdvSearch(element, id){
    var object = $(element).parent().parent().parent().parent().find('.filter_header');
    if (object.is(':visible')){
        closeAndClearAdvSearch(id);
    }
    else {
        $(element).parent().parent().parent().parent().find('.filter_header').show();
    }
    return false;
}
