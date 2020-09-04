class Solution:
    def validIPAddress(self, IP):
        if IP.count('.') == 3:
            return self._is_ipv4(IP)
        elif IP.count(':') == 7:
            return self._is_ipv6(IP)
        else:
            return 'Neither'
            

    def _is_ipv4(self, IP):
        ip_digits = IP.split('.')
        if '' in ip_digits:
            return 'Neither'
        for digit in ip_digits:
            if (digit.startswith('0') and len(digit) > 1) or not digit.isdigit() or int(digit) > 255 or int(digit) < 0:
                return 'Neither'
        return 'IPv4'

    def _is_ipv6(self, IP):
        hexdigits = '0123456789abcdefABCDEF'  # 16进制允许使用的字符

        ip_digits = IP.split(':')
        if '' in ip_digits:
            return 'Neither'
        for digit in ip_digits:
            if len(digit) > 4 or not all(char in hexdigits for char in digit):
                return 'Neither'
        return 'IPv6'

# ip = "172.16.254.1"
# ip = "1e1.4.5.6"
ip = "172.16.254.1"
# ip_2 = "2001:0db8:85a3:0:0:8A2E:0370:7334"
s = Solution()
print(s.validIPAddress(ip))
# print(s.validIPAddress(ip_2))

