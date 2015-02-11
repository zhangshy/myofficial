from models import User, UserReferPage, ImageCarousel, ImageVote

def getDataFromDB(username):
    user_id = User.query.filter_by(name=username).first().id
    print('in getDataFromDB:%d' % user_id)
    images = []
    tmp_carousels = ImageCarousel.query.filter_by(user_id=user_id)
    for tmp_carousel in tmp_carousels:
        image_carousel={}
        image_carousel['src'] = tmp_carousel.src;
        image_carousel['alt'] = tmp_carousel.alt;
        image_carousel['title'] = tmp_carousel.title;
        image_carousel['desc'] = tmp_carousel.desc;
        images.append(image_carousel)

    vImages=[]
    tmp_votes = ImageVote.query.filter_by(user_id=user_id)
    for tmp_vote in tmp_votes:
        image_vote = {}
        image_vote['src'] = tmp_vote.src
        image_vote['votes'] = tmp_vote.votes
        image_vote['id'] = tmp_vote.id
        vImages.append(image_vote)

    refers = []
    tmp_refers = UserReferPage.query.filter_by(user_id=user_id)
    for tmp_refer in tmp_refers:
        refer = {}
        refer['avatar'] = tmp_refer.avatar
        refer['href'] = tmp_refer.href
        refer['alt'] = tmp_refer.alt
        refers.append(refer)

    body={}
    body['images'] = images
#    body['refers'] = refers
    body['weibo'] = refers[0]
    body['zhibo'] = refers[1]
    body['vImages'] = vImages
    return body
