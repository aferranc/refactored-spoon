// Configure DataTable
$(document).ready(function() {
    var table = $('#restaurantTable').DataTable({
        // Configure column definitions
        "columnDefs": [
            { "searchable": false, "targets": 6 }  // Disable search in the "Actions" column
        ],
        // Set the initial order of the columns
        order: [[0, 'asc'], [2, 'asc']],
        // Configure the layout of the DataTable
        layout: {
            topStart: {
                pageLength: {
                    menu: [5, 10, 25, 50]
                }
            },
            topEnd: {
                search: {
                    processing: true
                }
            },
            bottomStart: {
                info: true  // Enable page info
            },
            bottomEnd: {
                paging: {
                    numbers: true  // Enable pagination with numbers
                }
            }
        }
    });
});
