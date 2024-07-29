import { defineStore } from "pinia";
import { parser } from "../repository/parser";
import { Notify } from "quasar";

export const useRealEstateParserStore = defineStore("realEstateParserStore", {
  state: () => ({
    loading: false, // Пока тру, идёт загрузка
    parser_links: null, // список страниц для парсера
    data_full_item: null, // спарсиные данные объявления
    data_task: null, // ранит данные о задаче
    /* Regions */
    list_regions: null,

    /* Фильтры */
    filters: {
      /* пагинация */
      limit: 10, // Количество постов на странице
      page: 1, // Номер текущей страницы
      size: 50, // количество items на страницу
      /* Фильтруем по полям таблицы */
      is_video: null, // items с видео
      status_id: 0, // статус items
      min_price: null, // минимальная цена items
      max_price: null, // максимальная цена items
    },
    error: [],
  }),

  /**
   * Действие с Items
   *
   * - получить список Items
   * - получить Item по ID или Link *Опционально
   * - изменить Item  с ID
   * - удалить  Item  с ID
   * - добавить Item
   */
  actions: {
    /**
     * получить список Items
     * @param {string} url
     * @param {object} params
     * {
        "min_price": 0,
        "max_price": 0,
        "status_id": 0,
        "is_video": false,
    }
     */
    async getLinks(filters = this.filters) {
      this.loading = true;
      try {
        this.error = [];
        let res = await parser.getItems(`/parsing/list`, filters);
        if (res.status == 500) {
          console.log(res.data.detail);
          this.error.push(res.data.detail);
          this.parser_links = [];
          Notify.create({
            message: res.data.detail,
            type: "negative",
            color: "negative",
            position: "bottom",
          });
        } else {
          this.parser_links = res;
        }
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async updateLink(data) {
      this.loading = true;
      try {
        this.error = [];
        let res = await parser.updateItem(
          `/parsing/edit/${data.id}?status_id=${data.status_id}&comment=${
            data.comment || ""
          }`
        );
        if (res.status == 500) {
          console.log(res.data.detail);
          this.error.push(res.data.detail);
          Notify.create({
            message: res.data.detail,
            type: "negative",
            color: "negative",
            position: "bottom",
          });
          return;
        }
        await this.getLinks();
      } catch (error) {
        console.log(error);
        this.loading = false;
      }
    },
    async cleanFilters() {
      this.filters = {
        /* пагинация */
        limit: 10, // Количество постов на странице
        page: 1, // Номер текущей страницы
        size: 50, // количество items на страницу
        /* Фильтруем по полям таблицы */
        is_video: null, // items с видео
        status_id: null, // статус items
        min_price: null, // минимальная цена items
        max_price: null, // максимальная цена items
      };
    },
    async callTaskGetFullData(id) {
      this.loading = true;
      try {
        this.error = [];
        let res = await parser.getItem(`/parsing/run/${id}`);
        if (res.status == 500) {
          console.log(res.data.detail);
          this.error.push(res.data.detail);
          this.data_task = null;
          Notify.create({
            message: res.data.detail,
            type: "negative",
            color: "negative",
            position: "bottom",
          });
        } else {
          this.data_task = res;
        }
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },

    async getResultTaskFullData(task_id) {
      this.loading = true;
      try {
        this.error = [];
        let res = await parser.getItem(`/parsing/tasks/${task_id}`);
        if (res.status == 500) {
          console.log(res.data.detail);
          this.error.push(res.data.detail);
          this.data_full_item = null;
          Notify.create({
            message: res.data.detail,
            type: "negative",
            color: "negative",
            position: "bottom",
          });
        } else {
          this.data_full_item = res;
        }
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getRegions() {
      this.loading = true;
      try {
        this.error = [];
        let res = await parser.getItems(`/real-estate/regions/`);
        if (res.status == 500) {
          console.log(res.data.detail);
          this.error.push(res.data.detail);
          this.parser_links = [];
          Notify.create({
            message: res.data.detail,
            type: "negative",
            color: "negative",
            position: "bottom",
          });
        } else {
          this.list_regions = res;
        }
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  },


  getters: {},
});
