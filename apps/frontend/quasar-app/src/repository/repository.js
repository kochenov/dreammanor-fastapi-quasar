import { api } from "boot/axios";

/*
 * перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error);
  }
);
/**
 *
 */
export const crud = {
  /**
   * Получение списка сущностей с сервера
   * @param {*} url
   * @param {*} filters
   * @returns
   */
  async getItems(url, filters) {
    try {
      let res = await api.get(url, {params: filters});
      return res.data;
    } catch (error) {
      console.log(error.response);
      return error.response;
    }
  },
  /**
   * Получение одной сущности с сервера
   * @param {*} url
   * @param {*} filters
   * @returns
   */
  async getItem(url, filters) {
    try {
      //let res = await api.get(url, {params: filters});
      //return res.data;
    } catch (error) {
      console.log(error.response);
      return error.response;
    }
  },
  /**
   * Запрос на сервер для изменения сущности
   * @param {*} url
   * @param {*} filters
   * @returns
   */
  async updateItem(url, data={}) {
    try {
      let res = await api.patch(url, data);
      return res.data;
    } catch (error) {
      console.log(error.response);
      return error.response;
    }
  },
  /**
   * Запрос на удаление сущности
   * @param {*} url
   * @param {*} filters
   * @returns
   */
  async deleteItem(url, filters) {
    try {
      let res = await api.get(url, {params: filters});
      return res.data;
    } catch (error) {
      console.log(error.response);
      return error.response;
    }
  },


};
