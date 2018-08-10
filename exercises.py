#List methods allow you to modify lists. The following are some list methods for you to practice with. Feel free to google resources to help you with this assignment.

#append(element) adds a single element to the list
#1. 'Anonymous' is also deserving to be in the hacker legends list. Add him in to the hacker legends list and print your results.

hacker_legends = ['LulzSec', 'Gary McKinnon', 'Adrian Lamo', 'Jonathan James', 'Kevin Poulsen']
hacker_legends.append('Anonymous')
print(hacker_legends)
#insert (index, element) adds a new element at any position in your list.
#2. You just created a networking study list and forgot to add in 'SSH'. Please add that into the 3rd position in the networking list and print your results.

networking = ['packet', 'LAN', 'WAN', 'port', 'firewall', 'VPN']
networking.insert(2,"SSH")
print(networking)
#remove(element) removes a single element from the list
#3. The cyber security analyst entered the wrong IP address in the list below. Please remove the non-float integer from the ip addy list and print your results.

ip_addy = [255.224, 192.168,  1331904083.25, 5102018, 10.255, 172.31]
ip_addy.remove(5102018)
print(ip_addy)
#pop(index) removes the element at the given index position
#4. The cyber traits list below is a list of traits that fit a career in cyber security. Everything is accurate, except for 'lazy'. Please remove 'lazy' from the list and print your results.

cyber_traits = ['detailed oriented', 'methodically', 'lazy', 'persistent', 'curious', 'instinctive']
cyber_traits.pop()
print(cyber_traits)
#extend(list) adds elements from another list 
#5. Combine the new co list with the sec co list and print your results.

sec_co = ['IBM', 'Raytheon', 'Mimecast', 'Cisco']
new_co= ['Checkp Point Software', 'Palo Alto Networks', 'Symantec', 'Trend Micro']
sec_co.extend(new_co)
print(sec_co)
#index(element) searches an element in the list and returns its index
#6. There were some headline grabbing cyber attacks in 2017. In the cyber attacks list below, find the index position of 'WannaCry' and print your result.

cyber_attacks = ['Equifax Data Breach', 'Uber Data Breach', 'Yahoo!','WannaCry', 'Deep Root Analytics']
print(cyber_attacks.index("WannaCry"))
#count(element) counts how many times an element is in a list
#7. In the dns list below, find the number of ocurrence for 98.105 and print your results.

dns_list = [98.105, 98.1115, 99.105, 98.111, 98.105, 98.106, 98.501]
print(dns_list.count(98.105))
#reverse() reverses the elements of a given list
#8. Decipher Mr. Robot's quote using the reverse method and print his message.

mr_robot = ['bigger', 'something', 'represents', 'it', 'mistake', 'a', 'just', 'never', 'is', 'bug', 'a']
mr_robot.reverse()
print(mr_robot)
#sort () sorts elements of a given list in a specific order (ascending or descending)
#9 Sort the following list of SSH Ids in ascending order

ssh_list = [1331903959.94555, 1331901011.84795, 1331903492.37203, 1331901032.03789, 1331903508.24007, 1331903476.8]
ssh_list.sort()
#print the list in descending order
print(ssh_list)
#max() returns the largest element in the list
#10 Find the largest integer in the network list below:

network_list = [39104, 38694, 38702, 38787, 39860]
print(max(network_list))
#min() returns the smallest element in the list
#11 Find the smallest integet in the network list below:

network_list = [39104, 38694, 38702, 38787, 39860]
print(min(network_list))
#sum() calculates the sum of the all the elements in the list
#12 Find the sum of the following occurence list below:

occurences = [3, 2.5, 9, 7, 21, 6, 8]
print(sum(occurences))


