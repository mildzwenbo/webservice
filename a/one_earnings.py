
class Earnings(object):

    def one_earnings(self, worth, new_worth):
        """
        累计收益率 = 最新净值 /初始净值-1
        年化收益率 = 累计收益率 x 一年的交易日数/净值最新日期与净值开始日期之间的交易日个数
        :param worth: 初始净值
        :param new_worth: 最新净值
        :return: year_accumulative ：年化收益率
        """
        accumulative = new_worth/worth-1  # 累计收益率
        year_accumulative = accumulative * 242/(6*21+15)  # 年化收益率
        return year_accumulative

    def child_fund_rate(self, child_fund, m_fund):
        """

        :param child_fund: 子基金市值
        :param m_fund: 母基金市值
        :return: 子基金占比
        """
        rate = child_fund/m_fund
        return rate


if __name__ == '__main__':
    r = Earnings()
    b = r.one_earnings(1.1630, 1.2257)
    # b = r.child_fund_rate(5000342.67, 90781370.94)
    print(b)
