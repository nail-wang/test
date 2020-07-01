import pytest
import yaml

def getdata():
    with open('test_data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

class TestCal:
    @pytest.mark.parametrize('a,b,result', getdata()['add'])
    def test_add(self, basic, a, b, result):
        assert result == basic.add(a , b)

    @pytest.mark.parametrize('a,b,result', getdata()['sub'])
    def test_sub(self, basic, a, b, result):
        assert result == basic.sub(a , b)

    @pytest.mark.parametrize('a,b,result', getdata()['mul'])
    def test_mul(self, basic, a, b, result):
        assert result == basic.mul(a , b)

    @pytest.mark.parametrize('a,b,result', getdata()['div'])
    def test_div(self, basic, a, b, result):
        assert result == basic.div(a , b)