from file_func import get_list_titles_not_my_posts, get_list_descriptions_my_posts


class TestPosts:

    def test_exists_not_my_post(self, get_token, get_info_not_my_post):
        assert get_info_not_my_post[1] in get_list_titles_not_my_posts(get_info_not_my_post[0], get_token)

    def test_create_my_post(self, create_my_post, get_token, get_info_my_post):
        assert get_info_my_post[1] in get_list_descriptions_my_posts(get_info_my_post[0], get_token)
