<template>
    <div>
        <vue-good-table
            :columns="columns"
            :rows="rows"
            compactMode

            :search-options="{
                enabled: true
            }"

            :pagination-options="{
                enabled: true,
                mode: 'records',
                perPage: 5,
                position: 'bottom',
                perPageDropdown: [3, 7, 9],
                dropdownAllowAll: false,
                setCurrentPage: 1,
                jumpFirstOrLast : true,
                firstLabel : 'First Page',
                lastLabel : 'Last Page',
                nextLabel: 'next',
                prevLabel: 'prev',
                rowsPerPageLabel: 'Rows per page',
                ofLabel: 'of',
                pageLabel: 'page', // for 'pages' mode
                allLabel: 'All',
                infoFn: (params) => `my own page ${params.firstRecordOnPage}`,
            }"

            @on-row-click="onRowClick"
        >
            <div slot="table-actions-bottom">
                This will show up on the bottom of the table.
            </div>
        </vue-good-table>
    </div>
</template>

<script>
import repos from "../assets/repos.json";

export default {
    name: 'MyTabelka',
    data() {
        return {
            columns: [
                {
                    label: 'Name',
                    field: 'name',
                },
                {
                    label: 'description',
                    field: 'Description',
                    type: 'number',
                },
                {
                    label: 'stars',
                    field: 'stars',
                    type: 'number',
                },
                {
                    label: 'forks',
                    field: 'forks',
                    type: 'number',
                },
                {
                    label: 'Updated on',
                    field: 'lastUpdatedAt',
                    type: 'date',
                    dateInputFormat: 'yyyy-MM-dd',
                    dateOutputFormat: 'MMM do yy',
                },

            ],
            rows: repos
        };
    },
    methods: {
        onRowClick(params) {
            // params.row - row object
            // params.pageIndex - index of this row on the current page.
            // params.selected - if selection is enabled this argument
            // indicates selected or not
            // params.event - click event

            console.log("a kuku!");
            console.log(params);
        }
    }
};
</script>
